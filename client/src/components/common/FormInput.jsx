import { FloatingLabel, Form } from "react-bootstrap";

const FormInput = ({ label, type, register, errors, name, placeholder, autoComplete }) => (
    <Form.Group className="mb-3">
        <FloatingLabel controlId={`form${name}`} label={label}>
            <Form.Control
                type={type}
                {...register(name)}
                placeholder={placeholder}
                autoComplete={autoComplete}
                isInvalid={!!errors[name]}
            />
            <Form.Control.Feedback type="invalid">
                {errors[name]?.message}
            </Form.Control.Feedback>
        </FloatingLabel>
    </Form.Group>
);

export default FormInput