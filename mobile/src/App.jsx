import { StatusBar } from 'expo-status-bar';
import { View } from 'react-native';
import Greeting from '@/components/common/Greeting';
import React from 'react';
import globalStyles from './themes/styles';

const App = () => {
	return (
		<View
			style={[
				globalStyles.container,
				{
					backgroundColor: 'lightblue',
				},
			]}>
			<Greeting />
			<StatusBar style='auto' />
		</View>
	);
};

export default App;
