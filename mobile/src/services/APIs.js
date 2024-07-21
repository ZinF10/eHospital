import { BASE_URL } from '@env';
import axios from 'axios';

const axiosInstance = axios.create({
    baseURL: BASE_URL,
    timeout: 1000,
});

console.info(BASE_URL)

export default axiosInstance;