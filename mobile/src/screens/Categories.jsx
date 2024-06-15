import globalStyles from "@/themes/styles";
import { StatusBar } from "expo-status-bar";
import { Text, View } from "react-native";

function Categories() {
  return (
    <View style={[globalStyles.container, { backgroundColor: "lightblue" }]}>
      <Text>Categories</Text>
      <StatusBar style="auto" />
    </View>
  );
}

export default Categories;
