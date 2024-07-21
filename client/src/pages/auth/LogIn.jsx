import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import { LoginSchema } from '@/utils/schemas';
import { useNavigate } from 'react-router-dom';
import useAuth from '@/hooks/customs/useAuth';
import { Alert, Button, Form } from 'react-bootstrap';
import { useState } from 'react';
import FormInput from '@/components/common/FormInput';

const LogIn = () => {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm({
        resolver: yupResolver(LoginSchema),
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const { login, isAuthenticated } = useAuth();
    const navigate = useNavigate();

    const onSubmit = async (data) => {
        setLoading(true);
        setError(null);
        const success = await login(data.username, data.password);
        setLoading(false);

        success ? (isAuthenticated() ?? navigate('/')) : setError('Đăng nhập không thành công. Vui lòng kiểm tra lại thông tin.');
    };

    return (
        <section className="mt-5">
            <h2>Đăng Nhập</h2>
            <Form onSubmit={handleSubmit(onSubmit)}>
                {error && <Alert variant="danger">{error}</Alert>}
                <FormInput 
                    label="Email" type="email" 
                    register={register} 
                    errors={errors} 
                    name={`username`} placeholder={'Nhập email'} 
                    autoComplete={"email"} 
                />
                <FormInput
                    label="Mật Khẩu" type="password"
                    register={register}
                    errors={errors}
                    name={`password`} placeholder={'Nhập mật khẩu'}
                    autoComplete={"current-password"}
                />
                <Button
                    variant="primary"
                    type="submit"
                    disabled={loading}
                >
                    {loading ? 'Đang xử lý…' : 'Đăng Nhập'}
                </Button>
            </Form>
        </section>
    )
}

export default LogIn