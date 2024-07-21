import Appointments from "screens/auth/Appointments";
import Profile from "screens/auth/Profile";
import About from "screens/core/About";
import Categories from "screens/core/Categories";
import Home from "screens/core/Home";
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';

const initialOptions = (title, iconName) => ({
    tabBarLabel: title,
    tabBarIcon: ({ color }) => (
        <MaterialCommunityIcons
            name={iconName}
            color={color}
            size={26} 
        />
    ),
});

const optionsHome = initialOptions('Home', 'home');
const optionsProfile = initialOptions('Profile', 'account');
const optionsAppointments = initialOptions('Appointments', 'stethoscope');

const RootRoutes = [
    {
        name: 'Home',
        component: Home,
        options: optionsHome
    },
    {
        name: 'Appointments',
        component: Appointments,
        options: optionsAppointments
    },
    {
        name: 'Profile',
        component: Profile,
        options: optionsProfile
    },
];

const DrawerRoutes = [
    {
        name: 'Categories',
        component: Categories
    },
    {
        name: 'About',
        component: About
    },
];

export { RootRoutes, DrawerRoutes };