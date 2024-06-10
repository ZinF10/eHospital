import routes from '@/routes/routes';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import React from 'react';

const Stack = createNativeStackNavigator();

const NativeStack = () => {
	return (
		<Stack.Navigator initialRouteName='Home'>
			{routes.map((route) => (
				<Stack.Screen
					key={route}
					name={route.name}
					component={route.component}
					options={route.options}
				/>
			))}
		</Stack.Navigator>
	);
};

export default NativeStack;
