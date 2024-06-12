import { createNativeStackNavigator } from '@react-navigation/native-stack';
import React from 'react';
import Setting from '@/screens/Setting';
import DrawerNavigator from './DrawerNavigator';

const Stack = createNativeStackNavigator();

const StackNavigator = () => {
    return (
        <Stack.Navigator>
            <Stack.Screen
                name="Root"
                component={DrawerNavigator}
                options={{ headerShown: false }}
            />
            <Stack.Screen name="Setting" component={Setting} />
        </Stack.Navigator>
    );
};

export default StackNavigator;
