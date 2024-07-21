import { useTheme } from 'hooks/contexts/ThemeContext';
import { View, Text } from 'react-native'
import createStyles from 'themes/styles'

const About = ({ navigation }) => {
    const [theme] = useTheme();
    const GlobalStyles = createStyles(theme)

    return (
        <View style={GlobalStyles.container}>
            <Text>About</Text>
        </View>
    )
}

export default About