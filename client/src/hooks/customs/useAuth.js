import cookie from 'react-cookies';
import endpoints from '@/services/endpoints';
import { useCurrentUser } from '../contexts/AuthContext';
import axiosInstance from '@/services/APIs';

const useAuth = () => {
    const [, dispatch] = useCurrentUser();

    const login = async (username, password) => {
        try {
            const data = {
                grant_type: 'password',
                client_id: 'RHdC0Fjp47c698qN7BDRsOIAKFE7rfCaxmV7Jnlk',
                client_secret:
                    '9RlTtDrVB8xN2Gl5ZqSKUZTxxB9XpHB4lzFpdocg47qOHJy3JnniDwrcIlpZEgbGGAn1l5l1zHrA2BRV2RcNYnUmhtiX4AArdhXTXXA7ixWPYcnhiVXHL1s0CCeGjvl2',
                username: username,
                password: password,
            };

            const response = await axiosInstance.post(
                endpoints['token'],
                data,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    },
                }
            );

            cookie.save(
                'access_token',
                response.data.access_token,
                { path: '/' },
            );

            const user = await axiosInstance.get(
                endpoints['current_user'],
                {
                    headers: {
                        Authorization: `Bearer ${cookie.load(
                            'access_token',
                        )}`,
                    },
                },
            );

            cookie.save('current_user', user.data, {
                path: '/',
            });

            dispatch({
                type: 'LOGIN',
                payload: user.data,
            });

            return true;
        } catch (error) {
            console.error('Error logging in:', error);
            return false;
        }
    };

    const logout = () => {
        dispatch({ type: 'LOGOUT' });
    };

    const isAuthenticated = () => {
        const accessToken = cookie.load('access_token');
        const currentUser = cookie.load('current_user');
        if (accessToken && currentUser) {
            return currentUser.is_doctor || currentUser.is_nurse;
        }
        return true;
    };

    return { login, logout, isAuthenticated };
};

export default useAuth;