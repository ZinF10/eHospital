const Footer = () => {
    return (
        <footer className="text-center">
            Bản quyền &copy; {new Date().getFullYear()} thuộc về {' '}
            <a href='https://github.com/zinitdev'>ZIN</a>.
        </footer>
    );
};

export default Footer;