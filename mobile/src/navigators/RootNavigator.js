import { createMaterialBottomTabNavigator } from "@react-navigation/material-bottom-tabs";
import { RootRoutes } from "routes/routes";

const Tab = createMaterialBottomTabNavigator();

const RootNavigator = () => {
    return (
        <Tab.Navigator
            initialRouteName="Home"
            activeColor="#2e86f2"
            inactiveColor="#595959"
            barStyle={{
                backgroundColor: '#fff',
            }}
        >
            {RootRoutes.map(route => (
                <Tab.Screen
                    key={route}
                    name={route.name}
                    component={route.component}
                    options={route.options}
                />
            ))}
        </Tab.Navigator>
    );
};

export default RootNavigator;