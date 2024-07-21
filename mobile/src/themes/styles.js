
import { StyleSheet } from "react-native";

const createStyles = (theme) => StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: theme.colors.background,
        alignItems: 'center',
        justifyContent: 'center'
    },
    text: {
        color: theme.colors.text
    },
    item: {
        backgroundColor: '#f9c2ff',
        padding: 20,
        marginVertical: 8,
    },
    header: {
        fontSize: 32,
        backgroundColor: theme.colors.primary,
        padding: 10,
    },
    title: {
        fontSize: 24,
        color: theme.colors.text,
        fontWeight: 'bold',
    },
})

export default createStyles