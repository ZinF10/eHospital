import { View, Text, Button } from 'react-native';
import createStyles from 'themes/styles';

const Appointments = ({ navigation }) => {
    const GlobalStyles = createStyles(theme)

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