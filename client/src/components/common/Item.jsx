import { Badge, Button, Card, Image, ListGroup } from 'react-bootstrap'
import { Link } from 'react-router-dom'

const Item = ({ item }) => {
    return (
        <Card>
            <Link className='text-decoration-none text-dark' to={`/search/${item.slug}`}>
                <Card.Body className="text-center">
                    <Image
                        className="rounded-circle"
                        width={60} height={60}
                        src={`${item.user.avatar}`}
                        alt={`${item.user.first_name}`}
                    />
                    <Card.Body className="py-2">
                        <Card.Title>{item.user.first_name}</Card.Title>
                        <Card.Text>
                            <Badge bg="info" className="p-2">
                                🩺 Tư vấn trực tiếp
                            </Badge>
                        </Card.Text>
                    </Card.Body>
                </Card.Body>
            </Link>
            <Card.Body className="bg-body-tertiary">
                <ListGroup className="mb-2">
                    <ListGroup.Item>
                        {item.tags.map((tag, idx) => (
                            <Badge bg="dark" key={idx} className="me-2">
                                {tag.name}
                            </Badge>
                        ))}
                    </ListGroup.Item>
                    <ListGroup.Item>Phòng khám {item.department}</ListGroup.Item>
                </ListGroup>
                <Button variant="outline-primary" className="w-100">Đặt lịch bác sĩ</Button>
            </Card.Body>
        </Card>
    )
}

export default Item