import { Card } from 'react-native-paper'

const Category = ({ category }) => {
    return (
        <Card>
            <Card.Title title={category.name} />
        </Card>
    )
}

export default Category