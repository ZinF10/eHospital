import { View, Text, StatusBar } from 'react-native'
import createStyles from 'themes/styles'

const Categories = () => {
    const GlobalStyles = createStyles(theme)

    return (
        <View style={[GlobalStyles.container, { backgroundColor: "lightblue" }]}>
            <Text>Categories</Text>
            <StatusBar style="auto" />
            
        </View>
    )
}

export default Categories