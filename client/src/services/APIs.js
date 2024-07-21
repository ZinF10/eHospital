import { BASE_URL } from '@/redux/constants/constants';
import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: BASE_URL,
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
    },
});

export default axiosInstance;