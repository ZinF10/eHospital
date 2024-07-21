import useAxios from '@/hooks/customs/useAxios';
import endpoints from '@/services/endpoints';
import { useCurrentUser } from '@/hooks/contexts/AuthContext';
import { Button, Container, Form, Nav, Navbar, NavDropdown } from 'react-bootstrap';
import { Link, NavLink, useNavigate } from 'react-router-dom';
import useAuth from '@/hooks/customs/useAuth';
import Each from '../common/Each';
import Avatar from '../common/Avatar';

const Header = () => {
    const [user] = useCurrentUser();
    const { data, isLoading } = useAxios(endpoints['categories']);
    const { logout } = useAuth();
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    return (
        <header>
            <Navbar collapseOnSelect expand="lg" bg="dark" data-bs-theme="dark" sticky="top">
                <Container>
                    <NavLink className={'navbar-brand'} to={'/'}>{process.env.REACT_APP_TITLE}</NavLink>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav className="me-auto">
                            <NavLink className={'nav-link'} to={'/'}>Trang Chủ</NavLink>
                            {data ? <NavDropdown title="Chuyên Mục" id="collapsible-nav-dropdown">
                                {isLoading ? <p>Đang tải dữ liệu...</p> : data && data.length > 0 ? (<Each
                                    of={data}
                                    render={(
                                        item,
                                        index,
                                    ) => (
                                        <NavLink key={index}
                                            className={'dropdown-item'}
                                            to={`medications/?category=${item.slug}`}>
                                            {
                                                item.name
                                            }
                                        </NavLink>
                                    )} />) :
                                    <NavDropdown.Item href="#">
                                        Không tìm thấy dữ liệu...
                                    </NavDropdown.Item>
                                }
                            </NavDropdown> : (
                                    <NavLink className={'nav-link'}>Chuyên Mục</NavLink>
                            )}
                            <NavLink className={'nav-link'} to={'/about'}>Giới Thiệu</NavLink>
                            <NavLink className={'nav-link'} to={'/contact'}>Liên Hệ</NavLink>
                        </Nav>
                        <Nav>
                            {user ? (<NavDropdown title={<Avatar user={user} size={28} />} id="auth-nav-dropdown">
                                <NavLink className={'dropdown-item'} to={'/profile'}>Hồ Sơ <span className={'text-success fst-italic'}>({user.last_name} {user.first_name})</span></NavLink>
                                <NavDropdown.Item onClick={handleLogout} >Đăng Xuất</NavDropdown.Item>
                            </NavDropdown>) : (
                                <NavDropdown title="Tài Khoản" id="log-nav-dropdown">
                                    <Link className={'dropdown-item'} to={'/login'}>Đăng Nhập</Link>
                                    <Link className={'dropdown-item'} to={'/register'}>Đăng Kí</Link>
                                </NavDropdown>
                            )}
                            <Form inline="true" className={'d-flex mt-2 mt-lg-0'}>
                                <Form.Control
                                    type="search"
                                    placeholder="Nhập từ khóa . . ."
                                    className="me-2"
                                    size="sm"
                                />
                                <Button variant="outline-success" size="sm" type="submit">Tìm</Button>
                            </Form>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
        </header>
    );
};

export default Header;