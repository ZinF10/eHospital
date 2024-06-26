import { ActivityIndicator, FlatList, StatusBar, Text, View } from 'react-native';
import React from 'react';
import GlobalStyles from 'themes/styles';
import useAxios from 'hooks/customs/useAxios';
import endpoints from 'services/endpoints';

const Home = () => {
    const { data, isLoading } = useAxios(endpoints['categories']);

    if (isLoading) {
        return <ActivityIndicator />;
    }

    return (
        <View style={GlobalStyles.container}>
            <StatusBar style="auto" />

            {data && data.length > 0 ? (
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
    )
}

export default Home