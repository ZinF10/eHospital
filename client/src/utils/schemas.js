import * as yup from 'yup';

const LoginSchema = yup
    .object()
    .shape({
        username: yup
            .string()
            .email('Invalid email')
            .required('Email is required'),
        password: yup.string().required('Password is required'),
    })
    .required();

export { LoginSchema }