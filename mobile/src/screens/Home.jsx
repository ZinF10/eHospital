import { View, Button } from 'react-native';
import React from 'react';
import Greeting from '@/components/common/Greeting';
import globalStyles from '@/themes/styles';
import { StatusBar } from 'expo-status-bar';

const Home = ({ navigation }) => {
    return (
        <View
            style={[
                globalStyles.container,
                {
                    backgroundColor: 'lightblue',
                },
            ]}
        >
            <Greeting />
            <Button
                title="View Appointments"
                onPress={() => navigation.navigate('Appointments')}
            />
            <StatusBar style="auto" />
        </View>
    );
};

export default Home;
