import useAxios from '@/hooks/useAxios';
import endpoints from '@/services/endpoints';
import globalStyles from '@/themes/styles';
import { StatusBar } from 'expo-status-bar';
import { ActivityIndicator, Text } from 'react-native';
import { Button, FlatList, View } from 'react-native';

function Home({ navigation }) {
    const { data, isLoading } = useAxios(endpoints['categories']);

    if (isLoading) {
        return <ActivityIndicator />;
    }

    return (
        <View
            style={[globalStyles.container, { backgroundColor: 'lightblue' }]}
        >
            <StatusBar style="auto" />

            {data ? (
                <FlatList
                    data={data}
                    keyExtractor={(item, index) => index.toString()}
                    renderItem={({ item }) => (
                        <View style={{ padding: 10 }}>
                            <Text>{item.name}</Text>
                        </View>
                    )}
                />
            ) : (
                <Text>No category</Text>
            )}
        </View>
    );
}

export default Home;
