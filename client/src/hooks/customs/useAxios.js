import axiosInstance from '@/services/APIs';
import { useCallback, useEffect, useState } from 'react';

const useAxios = (url) => {
    const [data, setData] = useState(null);
    const [isLoading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const loadingAxios = useCallback(async () => {
        try {
            setLoading(true);
            const response = await axiosInstance.get(url);
            setData(response.data.results || response.data);
            setError(null);
        } catch (error) {
            setError(error.message || 'Something went wrong');
        } finally {
            setLoading(false);
        }
    }, [url]);

    useEffect(() => {
        loadingAxios();
    }, [loadingAxios]);

    return { data, error, isLoading };
};

export default useAxios;