import { createContext, useCallback, useContext, useMemo, useState } from 'react';
import { DarkTheme, DefaultTheme } from 'themes/themes';

const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
    const [isDarkTheme, setIsDarkTheme] = useState(false);

    const toggleTheme = useCallback(() => {
        setIsDarkTheme((prevTheme) => !prevTheme);
    }, []);

    const theme = useMemo(() => (isDarkTheme ? DarkTheme : DefaultTheme), [isDarkTheme]);

    return (
        <ThemeContext.Provider value={[toggleTheme, theme, isDarkTheme]}>
            {children}
        </ThemeContext.Provider>
    );
};

export const useTheme = () => useContext(ThemeContext);

export default ThemeContext;