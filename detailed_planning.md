# Detailed Planning and Research for Zitouna Tamkeen Application Enhancements

## Phase 1: Detailed Planning and Research

This phase focuses on thoroughly understanding and documenting each new requirement, researching appropriate technologies, and outlining the implementation strategy for the initial UI and navigation fixes.

### 1.1 Analysis of Broken Navigation & UI Elements

#### 1.1.1 "Commencer votre demande" Button

**Current State:** The "Commencer votre demande" button on the homepage currently does not route to a dynamic guide form. It is a static button.

**Required Fix:** The button needs to be updated to navigate to a dynamic guide form. This implies that there will be a mechanism to select or identify the appropriate guide based on context (e.g., a specific service selected by the user, or a default guide).

**Implementation Plan:**
1. Identify the target route for the dynamic guide form (e.g., `/guides/new` or `/guide/:id`).
2. Update the `onClick` handler or `Link` component for this button in `App.jsx` (or the relevant component) to navigate to the correct route.
3. Ensure that the dynamic guide form component is capable of receiving parameters (if any) to load the correct guide.

#### 1.1.2 "En savoir plus" Buttons

**Current State:** The "En savoir plus" buttons under the service details (Microfinancement, MicroTakaful, etc.) are currently static and do not expand service details. They might be simple buttons or links that don't trigger any dynamic content display.

**Required Fix:** These buttons must trigger the expansion of service details, either through a collapsible section (accordion-style) or a modal dialog. This will provide users with more information about each service without navigating to a new page.

**Implementation Plan:**
1. For each service card, implement a state variable to control the visibility of the detailed information.
2. When an "En savoir plus" button is clicked, toggle this state variable.
3. Use a conditional rendering approach to show/hide the detailed content. Consider using a UI component library (like Shadcn/UI's `Collapsible` or `Dialog`) for a clean implementation.
4. Populate the detailed content with relevant information about each service.

#### 1.1.3 Hamburger Menu

**Current State:** The hamburger menu (on mobile view) is intended to show navigation links (Accueil, Guides, Profil, Admin, Paramètres). Based on previous interactions, the mobile navigation is already present at the bottom, but the request specifically mentions a 


hamburger menu, which implies a sidebar or overlay menu for mobile.

**Required Fix:** The hamburger menu must correctly display all primary navigation links (Accueil, Guides, Profil, Admin, Paramètres) when activated. This suggests a mobile-specific navigation component that slides in or overlays the content.

**Implementation Plan:**
1. Review the existing mobile navigation implementation. If it's a bottom bar, consider if a traditional hamburger menu (sidebar) is also desired or if the bottom bar is sufficient and the request implies enhancing its functionality.
2. Assuming a sidebar/overlay menu is desired, implement a state to control its open/close status.
3. Create a new component for the sidebar navigation, containing the `Accueil`, `Guides`, `Profil`, `Admin`, and `Paramètres` links.
4. Integrate this sidebar component with the hamburger icon, so clicking the icon toggles the sidebar visibility.
5. Ensure proper styling and responsiveness for the sidebar, including an overlay to dim the main content when the sidebar is open.

#### 1.1.4 Button States and Accessibility

**Current State:** Buttons might lack proper visual feedback for hover/active states and may not be fully keyboard-accessible.

**Required Fix:** All interactive buttons must have clear visual hover and active states. They must also be keyboard-accessible, meaning users can navigate to them using the Tab key and activate them with Enter or Space.

**Implementation Plan:**
1. Review the existing CSS for button styles. Ensure `:hover` and `:active` pseudo-classes are defined with appropriate visual changes (e.g., background color change, slight scale, shadow).
2. Verify that all buttons are rendered using `<button>` tags or `<a>` tags with `role="button"` and `tabIndex="0"` if they are custom components.
3. Test keyboard navigation by tabbing through the application and activating buttons with the Enter/Space key.
4. For custom components, ensure they correctly handle `onKeyDown` events for Enter/Space to trigger the `onClick` functionality.

### 1.2 Build the Guide Flow (Dynamic Form per Service)

This section details the design and implementation of the dynamic guide forms, which are central to the user's ability to submit documents for various services.

#### 1.2.1 Reusable Guide Component

**Requirement:** Create a reusable guide component that can load the correct service, show step-by-step instructions, collect user inputs (text, dropdown, file upload), validate required fields, and save progress locally.

**Implementation Plan:**
1. **Component Structure:** Design a single `GuideForm` component that can dynamically render different steps and input fields based on a configuration or data fetched from the backend.
2. **Dynamic Loading:** The component should accept a `serviceId` or `guideId` as a prop or extract it from the URL. Based on this ID, it will fetch the corresponding guide definition from the backend.
3. **Step-by-Step Instructions:** Each guide definition will include an array of steps. The component will manage the current step, allowing users to navigate forward and backward.
4. **Input Collection:** For each step, define the types of inputs required (text, number, dropdown, file upload). Use controlled components in React to manage form state.
   - **Text/Number Inputs:** Standard HTML `<input>` elements with `onChange` handlers.
   - **Dropdowns:** Standard HTML `<select>` elements or a custom dropdown component from Shadcn/UI.
   - **File Upload:** Implement a dedicated file upload component that handles file selection, preview, and validation. This component will interact with the backend for actual file storage.
5. **Validation:** Implement client-side validation for required fields and specific input formats (e.g., email, phone number). Provide clear error messages to the user.
6. **Local Progress Saving:** Use `localStorage` or `sessionStorage` to save the user's progress for the current guide. This will allow users to close the application and resume their progress later. The saved data should be associated with the user's ID and the specific guide ID.

#### 1.2.2 "Submit" Button Functionality

**Requirement:** The "Submit" button must upload all documents to the backend, create an application entry, and show a confirmation with a tracking ID.

**Implementation Plan:**
1. **Document Upload:** Before submitting the form, all uploaded files need to be sent to a secure backend endpoint. This will likely involve a multi-part form data request. The backend will store these files (e.g., in AWS S3 or Supabase Storage) and return their unique identifiers.
2. **Application Entry Creation:** Once documents are uploaded and their IDs are obtained, the form data (including document IDs) will be sent to another backend endpoint to create a new application entry in the database.
3. **Confirmation and Tracking ID:** Upon successful application creation, the backend will return a unique tracking ID. The frontend will display a confirmation message to the user, including this tracking ID, and clear the local progress data for that guide.

### 1.3 User Authentication & Profile

This section outlines the implementation of a robust user authentication system and the user profile management features.

#### 1.3.1 Full Backend Authentication

**Requirement:** Implement full backend authentication including signup (email/phone + password), login (with JWT or session), and password reset (via email/SMS).

**Implementation Plan:**
1. **Backend API Endpoints:** Develop RESTful API endpoints for:
   - `/api/auth/signup`: To register new users. Will require email/phone and password. Implement password hashing (e.g., bcrypt).
   - `/api/auth/login`: To authenticate users. Upon successful login, generate a JSON Web Token (JWT) or create a session and return it to the client.
   - `/api/auth/forgot-password`: To initiate password reset. This will send a unique token to the user's email or phone number.
   - `/api/auth/reset-password`: To allow users to set a new password using the token.
2. **Database Schema:** Design a `users` table in the database to store user credentials (hashed passwords), personal information, and authentication-related data.
3. **Frontend Integration:** Create React components for signup, login, and password reset forms. Use `axios` or `fetch` to interact with the backend API. Store the JWT/session token securely (e.g., in `localStorage` or `sessionStorage` for web, or secure storage for React Native if it were a native app).
4. **JWT/Session Management:** Implement logic to attach the JWT to all authenticated requests to the backend. Implement token refresh mechanisms if using short-lived JWTs.

#### 1.3.2 Connect "Modifier les informations"

**Requirement:** Allow users to edit their profile (name, phone, address, etc.) and save changes to the backend.

**Implementation Plan:**
1. **Backend API Endpoint:** Create a `/api/users/profile` (or similar) endpoint that allows authenticated users to update their profile information. This endpoint should validate input and update the `users` table.
2. **Frontend Profile Page:** Develop a "Profile" page in the React application where users can view and edit their personal details. Pre-populate the form fields with existing user data fetched from the backend.
3. **Form Submission:** Implement a form submission handler that sends the updated profile data to the backend API. Provide user feedback on success or failure.

#### 1.3.3 Show Real Application Statuses

**Requirement:** Fetch real application statuses from the backend and display a timeline (submitted → under review → approved/rejected).

**Implementation Plan:**
1. **Backend API Endpoint:** Create a `/api/applications` endpoint that returns a list of applications for the authenticated user, including their current status and a history of status changes.
2. **Database Schema:** Enhance the `applications` table to include a `status` field (e.g., enum: `submitted`, `under_review`, `approved`, `rejected`) and potentially a `status_history` (JSONB or separate table) to track changes over time.
3. **Frontend Display:** On the user's profile or a dedicated "My Applications" page, fetch this data and display it in a user-friendly format. Use a timeline component or similar UI element to visualize the application's journey through different statuses.

### 1.4 Admin Dashboard (Backend + Frontend)

This section details the development of a comprehensive admin dashboard for managing users, applications, and guides.

#### 1.4.1 Admin Login Route

**Requirement:** Create a separate admin login route (distinct from client login).

**Implementation Plan:**
1. **Separate Route:** Implement a dedicated login route for administrators (e.g., `/admin/login`). This route will use the same authentication mechanism but might have different UI or additional checks for admin roles.
2. **Role-Based Access Control (RBAC):** Implement RBAC in the backend to differentiate between regular users and administrators. Only users with the `admin` role should be able to access admin-specific API endpoints and frontend routes.

#### 1.4.2 Admin Functionalities

**Requirement:** Admin must be able to view all users and their applications, filter by status, service, or date, update application status (with notes), manage guides (add/edit/delete services), and manage users (reset password, deactivate).

**Implementation Plan:**
1. **Backend API Endpoints (Admin-specific):**
   - `/api/admin/users`: To fetch all users, with filtering and pagination options.
   - `/api/admin/users/:id/reset-password`: To reset a user's password.
   - `/api/admin/users/:id/deactivate`: To deactivate a user account.
   - `/api/admin/applications`: To fetch all applications, with filtering by status, service, date, and pagination.
   - `/api/admin/applications/:id/update-status`: To update an application's status, including an optional `notes` field.
   - `/api/admin/guides`: To manage guide definitions (CRUD operations).
2. **Frontend Admin Dashboard:** Develop a multi-section admin dashboard:
   - **Users Section:** Display a table of all users with search, filter, and pagination. Include actions for resetting passwords and deactivating accounts.
   - **Applications Section:** Display a table of all applications with search, filter, and pagination. Allow admins to view application details and update their status with notes.
   - **Guides Section:** Provide an interface for creating, editing, and deleting guide definitions. This will involve dynamic form builders for defining steps, input types, and required documents for each guide.
3. **Real Data:** Ensure all admin views and functionalities interact with the actual backend database, removing all mockup data.

### 1.5 File Upload & Document Handling

This section focuses on the secure and efficient handling of file uploads.

#### 1.5.1 Secure File Upload Endpoint

**Requirement:** Add a secure file upload endpoint that accepts PDF, JPG, PNG, limits file size (e.g., 5MB), and stores files in a cloud storage solution (e.g., AWS S3 or Supabase Storage).

**Implementation Plan:**
1. **Backend Endpoint:** Create a dedicated API endpoint (e.g., `/api/upload`) that handles file uploads. This endpoint should:
   - Validate file types (MIME types: `application/pdf`, `image/jpeg`, `image/png`).
   - Enforce file size limits (e.g., 5MB).
   - Sanitize filenames to prevent path traversal or other security vulnerabilities.
   - Integrate with a cloud storage SDK (AWS S3 SDK or Supabase Storage client) to upload the files securely.
   - Return the public URL or a unique identifier for the stored file.
2. **Cloud Storage Setup:** Configure an AWS S3 bucket or Supabase Storage bucket with appropriate access policies (e.g., private by default, public access only for specific URLs).
3. **Link Files to User/Application:** The backend should associate the uploaded file with the `userId` and `applicationId` in the database. This might involve adding a `documents` table or a JSONB field in the `applications` table.

#### 1.5.2 File Upload UI/UX

**Requirement:** Show an upload progress bar and allow re-upload if rejected.

**Implementation Plan:**
1. **Progress Bar:** In the frontend file upload component, implement a progress bar that updates in real-time as the file is being uploaded. This can be achieved by listening to progress events from the `axios` or `fetch` request.
2. **Re-upload Mechanism:** If an application is rejected due to missing or incorrect documents, the user should be able to re-upload specific documents. This implies that the guide form should allow editing previously submitted documents or adding new ones for rejected applications.

### 1.6 Notifications (In-App + Email/SMS)

This section details the implementation of a comprehensive notification system.

#### 1.6.1 Build Notification System

**Requirement:** Build a notification system that triggers on application submission, status changes, and missing documents. Allow users to enable/disable in-app notifications (priority), email (optional), and SMS (optional). Store preferences in the backend per user.

**Implementation Plan:**
1. **Backend Notification Service:** Create a backend service responsible for generating and sending notifications. This service will:
   - Listen for specific events (e.g., new application, status update, document rejection).
   - Fetch user notification preferences from the database.
   - Send notifications via:
     - **In-app:** Store notifications in a `notifications` table in the database, linked to the `userId`. The frontend will poll this table or use WebSockets for real-time updates.
     - **Email:** Integrate with an email service provider (e.g., SendGrid, Mailgun) to send email notifications. Use templates for different notification types.
     - **SMS:** Integrate with an SMS gateway (e.g., Twilio) to send SMS notifications.
2. **Database Schema:** Add a `notifications` table (for in-app notifications) and a `user_preferences` table (or fields in `users` table) to store notification preferences.
3. **Frontend Notification Display:** Implement an in-app notification center where users can view their notifications. Provide UI toggles in the user profile settings to manage email and SMS preferences.

### 1.7 Security & 2FA

This section focuses on enhancing the application's security posture.

#### 1.7.1 Enable 2FA (TOTP or SMS)

**Requirement:** Enable 2FA (TOTP or SMS) as optional for users and required for admins.

**Implementation Plan:**
1. **Backend 2FA Implementation:**
   - **TOTP (Time-based One-Time Password):** Integrate a TOTP library (e.g., `pyotp` for Python, `speakeasy` for Node.js) to generate and verify TOTP codes. Users will scan a QR code with an authenticator app (e.g., Google Authenticator).
   - **SMS 2FA:** Integrate with an SMS gateway (e.g., Twilio) to send SMS codes for 2FA. This will be an alternative to TOTP.
2. **Frontend 2FA Setup:** Develop UI for users to enable/disable 2FA, including displaying QR codes for TOTP setup and input fields for SMS verification codes.
3. **Admin 2FA Enforcement:** For admin login, enforce 2FA as mandatory. If an admin tries to log in without 2FA enabled, prompt them to set it up.

#### 1.7.2 Password Management and Security

**Requirement:** Add a password change flow (old password → new password → confirm), use HTTPS only (force redirect), and rate-limit login attempts.

**Implementation Plan:**
1. **Password Change Flow:** Implement a backend endpoint (e.g., `/api/auth/change-password`) that requires the old password, new password, and new password confirmation. The backend will verify the old password before updating it.
2. **HTTPS Enforcement:** Configure the web server (e.g., Nginx, Apache) or the deployment platform to force HTTPS redirects for all HTTP traffic. Ensure all internal API calls also use HTTPS.
3. **Rate Limiting:** Implement rate limiting on the login endpoint (and potentially other sensitive endpoints) to prevent brute-force attacks. Use a library or middleware (e.g., `express-rate-limit` for Node.js, `Flask-Limiter` for Flask) to limit the number of login attempts from a single IP address within a given time frame.

### 1.8 Responsive & Accessibility Fixes

This section focuses on ensuring a consistent and accessible user experience across all devices.

#### 1.8.1 Mobile/Tablet Responsiveness

**Requirement:** Test on mobile/tablet and fix layout issues.

**Implementation Plan:**
1. **Cross-Device Testing:** Conduct thorough testing on various mobile and tablet devices (or use browser developer tools to simulate different screen sizes).
2. **CSS Adjustments:** Identify and fix layout issues using CSS media queries, Flexbox, and Grid. Ensure elements stack correctly, text remains readable, and interactive elements are easily tappable.
3. **Viewport Meta Tag:** Verify the `viewport` meta tag in `index.html` is correctly configured for responsive behavior.

#### 1.8.2 Accessibility Enhancements

**Requirement:** Add ARIA labels for screen readers and ensure keyboard navigation works on all forms.

**Implementation Plan:**
1. **ARIA Labels:** Add appropriate `aria-label`, `aria-labelledby`, `aria-describedby`, and `role` attributes to interactive elements, form fields, and dynamic content to improve screen reader compatibility.
2. **Keyboard Navigation:** Ensure that all interactive elements (buttons, links, form fields) are reachable via the Tab key and can be activated using Enter or Space. Pay special attention to custom components to ensure they correctly handle keyboard events.
3. **Focus Management:** Implement proper focus management for modal dialogs, sidebars, and other dynamic UI elements to ensure a logical tab order.

### 1.9 Testing & QA

This section outlines the comprehensive testing and quality assurance procedures.

#### 1.9.1 Test Cases

**Requirement:** Create test cases for each service guide, test file upload on slow networks, test with 3 real users (observe confusion points), and test admin actions (update status, delete user, etc.).

**Implementation Plan:**
1. **Service Guide Test Cases:** Develop detailed test cases for each step of every service guide, covering:
   - Valid and invalid input scenarios.
   - Required field validation.
   - File upload success and failure (wrong type, too large).
   - Progress saving and resuming.
   - Navigation between steps.
2. **File Upload Network Testing:** Simulate slow network conditions (using browser developer tools or network throttling tools) and test file uploads to ensure robustness and proper error handling.
3. **User Acceptance Testing (UAT):** Recruit 3 real users to test the application. Observe their interactions, identify confusion points, and gather feedback on usability and clarity. Document all issues and suggestions.
4. **Admin Action Testing:** Thoroughly test all admin functionalities:
   - User management (create, view, edit, deactivate, reset password).
   - Application management (view, filter, update status, add notes).
   - Guide management (create, edit, delete guides).

### 1.10 Final Launch Prep

This section covers the final steps before launching the application.

#### 1.10.1 Legal and Support Documentation

**Requirement:** Write privacy policy & terms of use, add contact/support email in footer, and create FAQ page with common questions.

**Implementation Plan:**
1. **Privacy Policy & Terms of Use:** Draft comprehensive privacy policy and terms of use documents. These should be accessible from the application (e.g., in the footer or a dedicated legal section).
2. **Contact/Support Information:** Add the contact/support email and phone number (as provided previously) to the application footer and a dedicated "Contact Us" page.
3. **FAQ Page:** Create an FAQ page with common questions and answers related to microfinance applications, document requirements, and application status.

#### 1.10.2 App Store Assets and Error Logging

**Requirement:** Create app store assets (if mobile) and set up error logging (e.g., Sentry).

**Implementation Plan:**
1. **App Store Assets (if applicable):** If the PWA is to be listed in app stores (e.g., Google Play Store via Trusted Web Activity), prepare necessary assets like screenshots, feature graphics, and promotional videos.
2. **Error Logging:** Integrate an error logging service (e.g., Sentry, Bugsnag) into both the frontend and backend to capture and monitor application errors in real-time. This will help in quickly identifying and resolving issues in production.

This detailed plan provides a roadmap for developing the enhanced Zitouna Tamkeen application. Each section outlines the current state, required fixes/features, and a high-level implementation strategy. The next phases will involve executing these plans, starting with backend setup and authentication.

