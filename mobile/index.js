import 'react-native-gesture-handler';
import { AppRegistry } from 'react-native';
import { name as appName } from './app.json';
import App from 'App';
import { PaperProvider } from 'react-native-paper';
import { ThemeProvider, useTheme } from 'hooks/contexts/ThemeContext';

export default function Main() {
    const theme = useTheme();

    return (
        <ThemeProvider>
            <PaperProvider them={theme}>
                <App />
            </PaperProvider>
        </ThemeProvider>
    )
}

AppRegistry.registerComponent(appName, () => Main);