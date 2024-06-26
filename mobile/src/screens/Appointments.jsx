import { View, Text, Button } from 'react-native';
import React from 'react';
import GlobalStyles from 'themes/styles';

const Appointments = ({ navigation }) => {
    return (
        <View
            style={[
                GlobalStyles.container,
                {
                    backgroundColor: 'lightblue',
                },
            ]}
        >
            <Text>Appointments</Text>
            <Button title="Go back" onPress={() => navigation.goBack()} />
        </View>
    );
};

export default Appointments;