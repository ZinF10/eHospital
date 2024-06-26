
import Appointments from 'screens/Appointments';
import Categories from 'screens/Categories';
import Home from 'screens/Home';
import Profile from 'screens/Profile';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';

const createTabOptions = (title, iconName) => ({
    tabBarLabel: title,
    tabBarIcon: ({ color }) => (
        <MaterialCommunityIcons name={iconName} color={color} size={26} />
    ),
});

const optionsHome = createTabOptions('Home', 'home');
const optionsProfile = createTabOptions('Profile', 'account');
const optionsAppointments = createTabOptions('Appointments', 'stethoscope');

const RootRoutes = [
    {
        name: 'Home', component: Home, options: optionsHome
    },
    {
        name: 'Appointments',
        component: Appointments,
        options: optionsAppointments,
    },
    { name: 'Profle', component: Profile, options: optionsProfile },
];

const DrawerRoutes = [
    { name: 'Categories', component: Categories },
    { name: 'Profle', component: Profile },
];

export { RootRoutes, DrawerRoutes };