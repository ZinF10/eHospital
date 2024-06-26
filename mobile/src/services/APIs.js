const { default: axios } = require('axios');
import { BASE_URL } from '@env';

const axiosInstance = axios.create({
    baseURL: BASE_URL,
    timeout: 1000,
});

export default axiosInstance;