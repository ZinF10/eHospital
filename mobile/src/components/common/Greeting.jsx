import { View, Text } from 'react-native';
import React from 'react';

const Greeting = () => {
	return (
		<View>
			<Text
				style={[
					{
						color: 'gray',
						fontSize: 32,
					},
				]}>
				Hello, Bro ✌️
			</Text>
			<Text
				style={[
					{
						color: 'white',
						fontSize: 20,
					},
				]}>
				Welcome to eHospital 💗
			</Text>
		</View>
	);
};

export default Greeting;
