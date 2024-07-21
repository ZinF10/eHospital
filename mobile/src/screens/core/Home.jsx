import { View, Text, ActivityIndicator } from 'react-native';
import createStyles from 'themes/styles';
import useAxios from 'hooks/customs/useAxios';
import endpoints from 'services/endpoints';
import NotFound from 'components/common/NotFound';
import { Switch } from 'react-native-paper';
import { useTheme } from 'hooks/contexts/ThemeContext';
import CategoriesSectionList from 'components/common/CategoriesSectionList';

const Home = () => {
  const [toggleTheme, theme, isDarkTheme] = useTheme();
  const { data, isLoading } = useAxios(endpoints['categories']);
  const GlobalStyles = createStyles(theme)

  return (
    <View style={GlobalStyles.container}>
      <Switch value={isDarkTheme} onValueChange={toggleTheme} />
      <Text style={GlobalStyles.text}>Welcome to &#128512;</Text>
      {isLoading ? (
        <ActivityIndicator size="large" color="#0000ff" />
      ) : (data && data.length > 0) ? (
        <CategoriesSectionList categories={data} />
      ) : (
        <NotFound />
      )}
    </View>
  );
}

export default Home;
