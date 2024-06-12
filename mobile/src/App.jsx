import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import NativeStack from './navigators/StackNavigator';

const App = () => {
    return (
        <NavigationContainer>
            <NativeStack />
        </NavigationContainer>
    );
};

export default App;
