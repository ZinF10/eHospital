import { useEffect, useRef } from 'react';

const useDocumentTitle = (title, path = '') => {
    const defaultTitle = useRef(document.title);

    useEffect(() => {
        document.title = title;
    }, [path, title]);

    useEffect(() => () => {
        document.title = defaultTitle.current;
    }, []);
};

export default useDocumentTitle;
