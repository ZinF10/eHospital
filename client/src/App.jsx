import { BrowserRouter, Route, Routes } from "react-router-dom";
import RootLayout from "@/components/layouts/RootLayout";
import { PrivateRoutes, PublicRoutes } from "@/routes/routes";
import PrivateRoute from "@/auth/PrivateRoute";
import { AuthProvider } from "@/hooks/contexts/AuthContext";

const App = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route element={<RootLayout title="Home" />}>
            {PublicRoutes.map((route) => {
              const Page = route.component;
              return (
                <Route
                  key={route}
                  path={route.path}
                  element={<Page />}
                  lazy={route.lazy}
                />
              );
            })}
            <Route element={<PrivateRoute />}>
              {PrivateRoutes.map((route) => {
                const Page = route.component;
                return (
                  <Route
                    key={route.path}
                    path={route.path}
                    element={<Page />}
                    lazy={route.lazy}
                  />
                );
              })}
            </Route>
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;