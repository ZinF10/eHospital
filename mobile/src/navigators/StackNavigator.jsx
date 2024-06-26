import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Settings from "screens/Settings";

const Stack = createNativeStackNavigator();

const StackNavigator = () => {
    return (
        <Stack.Navigator>
            <Stack.Screen name="Settings" component={Settings} />
        </Stack.Navigator>
    )
}

export default StackNavigator