import { createNativeStackNavigator } from "@react-navigation/native-stack";
import About from "screens/core/About";
import Home from "screens/core/Home";

const Stack = createNativeStackNavigator();

const StackNavigator = () => {
    return (
        <Stack.Navigator initialRouteName="Home">
            <Stack.Screen
                name="Home"
                component={Home}
                options={{ title: 'Welcome' }}
            />
            <Stack.Screen
                name="About"
                component={About}
                options={{ title: 'About' }}
            />
        </Stack.Navigator>
    )
}

export default StackNavigator