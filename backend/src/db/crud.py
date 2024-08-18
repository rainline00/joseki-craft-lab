from memgraph_db import MemgraphConnection
from src.models.position import Move, Position


class PositionCRUD:
    @staticmethod
    async def create_position(sfen, evaluation=None, best_move=None):
        connection = await MemgraphConnection.get_connection()
        connection.execute(
            """
            CREATE (p:Position {sfen: $sfen, evaluation: $evaluation, best_move: $best_move})
            """,
            {"sfen": sfen, "evaluation": evaluation, "best_move": best_move},
        )
        return Position(sfen=sfen, evaluation=evaluation, best_move=best_move)

    @staticmethod
    async def get_position_by_sfen(sfen):
        connection = await MemgraphConnection.get_connection()
        result = connection.execute_and_fetch(
            """
            MATCH (p:Position {sfen: $sfen})
            RETURN p
            """,
            {"sfen": sfen},
        )
        position_data = None
        for record in result:
            position_data = record["p"]
        if position_data:
            return Position(**position_data)
        return None

    @staticmethod
    async def update_position(sfen, evaluation=None, best_move=None):
        connection = await MemgraphConnection.get_connection()
        query = """
        MATCH (p:Position {sfen: $sfen})
        SET p.evaluation = COALESCE($evaluation, p.evaluation),
            p.best_move = COALESCE($best_move, p.best_move)
        RETURN p
        """
        params = {"sfen": sfen, "evaluation": evaluation, "best_move": best_move}
        result = connection.execute_and_fetch(query, params)
        updated_position = None
        for record in result:
            updated_position = record["p"]
        if updated_position:
            return Position(**updated_position)
        return None

    @staticmethod
    async def delete_position(sfen):
        connection = await MemgraphConnection.get_connection()
        connection.execute(
            """
            MATCH (p:Position {sfen: $sfen})
            DETACH DELETE p
            """,
            {"sfen": sfen},
        )


class MoveCRUD:
    @staticmethod
    async def create_move(start_position, end_position, move_string, count=1):
        connection = await MemgraphConnection.get_connection()
        connection.execute(
            """
            MATCH (start:Position {sfen: $start_sfen}), (end:Position {sfen: $end_sfen})
            CREATE (start)-[:Move {move_string: $move_string, count: $count}]->(end)
            """,
            {
                "start_sfen": start_position.sfen,
                "end_sfen": end_position.sfen,
                "move_string": move_string,
                "count": count,
            },
        )
        return Move(start_position=start_position, end_position=end_position, move_string=move_string, count=count)

    @staticmethod
    async def get_moves_by_start_position(sfen):
        connection = await MemgraphConnection.get_connection()
        result = connection.execute_and_fetch(
            """
            MATCH (p1:Position {sfen: $sfen})-[m:Move]->(p2:Position)
            RETURN m, p2
            """,
            {"sfen": sfen},
        )
        moves = []
        for record in result:
            move_data = record["m"]
            end_position_data = record["p2"]
            move = Move(
                start_position=Position(sfen=sfen),
                end_position=Position(**end_position_data),
                move_string=move_data["move_string"],
                count=move_data["count"],
            )
            moves.append(move)
        return moves

    @staticmethod
    async def update_move(start_position, end_position, move_string, count=None):
        connection = await MemgraphConnection.get_connection()
        connection.execute(
            """
            MATCH (p1:Position {sfen: $start_sfen})-[m:Move {move_string: $move_string}]->(p2:Position {sfen: $end_sfen})
            SET m.count = COALESCE($count, m.count)
            """,
            {
                "start_sfen": start_position.sfen,
                "end_sfen": end_position.sfen,
                "move_string": move_string,
                "count": count,
            },
        )

    @staticmethod
    async def delete_move(start_position, end_position, move_string):
        connection = await MemgraphConnection.get_connection()
        connection.execute(
            """
            MATCH (p1:Position {sfen: $start_sfen})-[m:Move {move_string: $move_string}]->(p2:Position {sfen: $end_sfen})
            DELETE m
            """,
            {"start_sfen": start_position.sfen, "end_sfen": end_position.sfen, "move_string": move_string},
        )
