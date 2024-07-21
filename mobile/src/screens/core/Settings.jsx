import { View, Button } from 'react-native'

const Settings = ({ navigation }) => {
    return (
        <View style={{ flex: 1, alignItems: "center", justifyContent: "center" }}>
            <Button title="Go back" onPress={() => navigation.goBack()} />
            <Button title="Go to Home" onPress={() => navigation.navigate("Home")} />
        </View>
    )
}

export default Settings