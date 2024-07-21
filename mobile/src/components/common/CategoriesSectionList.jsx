import { View } from 'react-native'
import { FlatList } from 'react-native-gesture-handler'
import Category from './Category'

const CategoriesSectionList = ({ categories, theme }) => {
    return (
        <FlatList
            data={categories}
            horizontal={true}
            keyExtractor={(category) => category.slug}
            renderItem={({ item }) => (
                <View style={{ paddingHorizontal: 10 }}>
                    <Category category={item} />
                </View>
            )}
        />
    )
}

export default CategoriesSectionList