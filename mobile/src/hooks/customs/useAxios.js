import { useCallback, useEffect, useState } from 'react';
import axiosInstance from 'services/APIs';

const useAxios = (url) => {
    const [data, setData] = useState([]);
    const [isLoading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const fetchData = useCallback(async () => {
        try {
            setLoading(true);
            const response = await axiosInstance.get(url);
            setData(response.data);
            setError(null);
        } catch (error) {
            setError(error.message || 'Something went wrong');
        } finally {
            setLoading(false);
        }
    }, [url]);

    useEffect(() => {
        fetchData();
    }, [fetchData]);

    return { data, error, isLoading };
};

export default useAxios;