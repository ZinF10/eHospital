import { View, Text } from 'react-native';
import React from 'react';
import globalStyles from '@/themes/styles';

const Profile = () => {
    return (
        <View style={[
                globalStyles.container,
                {
                    backgroundColor: 'lightblue',
                },
            ]}>
            <Text>Profile</Text>
        </View>
    );
};

export default Profile;
