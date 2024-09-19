import React, { ReactNode } from 'react';
import { Header } from '../Header/Header';
import { NavBar } from '../NavBar/NavBar';
import { Footer } from '../Footer/Footer';

interface LayoutProps {
  children: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    // Render a main container element
    <div className="layout-container">
      {/* Render the Header component at the top */}
      <Header />

      {/* Render the NavBar component below the header */}
      <NavBar />

      {/* Render the main content (passed as children) in the center */}
      <main className="main-content">
        {children}
      </main>

      {/* Render the Footer component at the bottom */}
      <Footer />
    </div>
  );
};

export default Layout;

// Human tasks:
// TODO: Implement styling and layout for the layout container and its components.
// TODO: Ensure responsiveness across different screen sizes.