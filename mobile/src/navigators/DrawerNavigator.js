import { createDrawerNavigator } from "@react-navigation/drawer";
import { DrawerRoutes } from "routes/routes";
import RootNavigator from "./RootNavigator";

const Drawer = createDrawerNavigator();

const DrawerNavigator = () => {
    return (
        <Drawer.Navigator initialRouteName="Root">
            <Drawer.Screen
                name="Root"
                component={RootNavigator}
                options={{ title: 'Home' }}
            />
            {DrawerRoutes.map(route => (
                <Drawer.Screen
                    key={route}
                    name={route.name}
                    component={route.component}
                />
            ))}
        </Drawer.Navigator>
    )
}

export default DrawerNavigator