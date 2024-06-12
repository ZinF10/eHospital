import routes from '@/routes/routes';
import { createMaterialBottomTabNavigator } from '@react-navigation/material-bottom-tabs';

const Tab = createMaterialBottomTabNavigator();

const TabNavigator = () => {
    return (
        <Tab.Navigator
            initialRouteName="Home"
            activeColor="#2e86f2"
            inactiveColor="#595959"
            barStyle={{
                backgroundColor: '#fff',
            }}
        >
            {routes.map(route => (
                <Tab.Screen
                    key={route}
                    name={route.name}
                    component={route.component}
                    options={route.options}
                />
            ))}
        </Tab.Navigator>
    );
}

export default TabNavigator