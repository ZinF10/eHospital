import { MD3DarkTheme, MD3LightTheme } from "react-native-paper";
import { DarkSchemes, LightSchemes } from "./schemes";

const DefaultTheme = {
    ...MD3LightTheme,
    colors: LightSchemes.colors,
};

const DarkTheme = {
    ...MD3DarkTheme,
    colors: DarkSchemes.colors
};

export { DefaultTheme, DarkTheme }