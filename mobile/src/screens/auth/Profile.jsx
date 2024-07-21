import { View, Button } from 'react-native'
import createStyles from 'themes/styles'

const Profile = ({ navigation }) => {
    const GlobalStyles = createStyles(theme)

    return (
        <View style={GlobalStyles.container}>
            <Button title="Go back" onPress={() => navigation.goBack()} />
        </View>
    )
}

export default Profile