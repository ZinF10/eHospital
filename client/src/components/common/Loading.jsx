import { Spinner } from "react-bootstrap"

const Loading = () => {
    return (
        <Spinner animation="border" role="status">
            <span className="visually-hidden">Đang xử lý...</span>
        </Spinner>
    )
}

export default Loading