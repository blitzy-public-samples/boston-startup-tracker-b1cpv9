import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-800 text-white py-6">
      <div className="container mx-auto px-4">
        <div className="flex flex-wrap justify-between items-center">
          {/* Copyright information */}
          <div className="w-full md:w-auto mb-4 md:mb-0">
            <p>&copy; {new Date().getFullYear()} Boston Startup Tracker. All rights reserved.</p>
          </div>

          {/* Footer links */}
          <nav className="w-full md:w-auto">
            <ul className="flex flex-wrap justify-center md:justify-end">
              <li className="mx-2"><a href="/about" className="hover:text-gray-300">About Us</a></li>
              <li className="mx-2"><a href="/contact" className="hover:text-gray-300">Contact</a></li>
              <li className="mx-2"><a href="/privacy" className="hover:text-gray-300">Privacy Policy</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

// Human tasks:
// - Populate the footer with actual content, including copyright information, links, and potentially social media icons.