import React, { createContext, useContext, useState, ReactNode } from 'react';

interface AppState {
  currentPosition: string;
}

interface AppContextType {
  state: AppState;
  setCurrentPosition: (position: string) => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [state, setState] = useState<AppState>({
    currentPosition: 'lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1',
  });

  const setCurrentPosition = (position: string) => {
    setState(prevState => ({ ...prevState, currentPosition: position }));
  };

  return (
    <AppContext.Provider value={{ state, setCurrentPosition }}>
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  return context;
};