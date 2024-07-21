import React from 'react'
import { Col, Row } from 'react-bootstrap'
import Item from './Item'

const ItemList = ({ doctors }) => {
    return (
        <Row xs={1} md={2} lg={4} className="g-4">
            {doctors.map((item, index) => (
                <Col key={index}>
                    <Item item={item} />
                </Col>
            ))}
        </Row>
    )
}

export default ItemList