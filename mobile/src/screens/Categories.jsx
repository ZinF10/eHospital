import { View, Text, StatusBar } from 'react-native'
import React from 'react'
import GlobalStyles from 'themes/styles'

const Categories = () => {
    return (
        <View style={[GlobalStyles.container, { backgroundColor: "lightblue" }]}>
            <Text>Categories</Text>
            <StatusBar style="auto" />
        </View>
    )
}

export default Categories