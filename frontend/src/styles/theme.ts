import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  // ここにカスタムテーマの設定を追加
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
  // その他のテーマ設定
});

export default theme;
