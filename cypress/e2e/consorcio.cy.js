const adminData = {
    username: "admin",
    email: "admin@example.com",
    password: "1234",
    isAdmin: true,
};

const baseUrl = 'http://127.0.0.1:8000'; // Use uma constante para a URL base

beforeEach(() => {
    // Limpa o banco de dados e executa as migrações
    cy.exec('rm -f db.sqlite3 || del /f db.sqlite3'); // Compatível com Unix e Windows
    cy.exec('venv/bin/python manage.py migrate');

    // Cria um usuário admin diretamente no banco de dados
    cy.exec(`venv/bin/python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('${adminData.username}', '${adminData.email}', '${adminData.password}')"`);
    
    // Espera o servidor estar pronto
    cy.wait(1000); // Aguarda um curto período antes de verificar o servidor
    cy.request(baseUrl)
      .its('status')
      .should('eq', 200);
});

describe('Testes de Condições da Cidade', () => {
    it('Admin: Deve acessar a página Consórcio de Culturas após login', () => {
        cy.visit(`${baseUrl}/login`);
        
        // Login como Admin
        cy.get('input[name="email"]').type(adminData.email);
        cy.get('input[name="password"]').type(adminData.password);
        cy.get('button[type="submit"]').click();
  
        // Verifica se o admin consegue acessar a página "Consórcio de Culturas"
        cy.visit(`${baseUrl}/rotacao/`); // Atualize o URL conforme necessário
        cy.contains('Consórcio de Culturas').should('be.visible'); // Verifica se a página carregou corretamente
    });

    it('Novo Usuário: Deve acessar a página Consórcio de Culturas após login', () => {
        // Registro de novo usuário
        cy.visit(`${baseUrl}/signup`);
        cy.get('input[name="username"]').type('usuario_valido');
        cy.get('input[name="email"]').type('usuario_valido@example.com');
        cy.get('input[name="password1"]').type('senha_valida123');
        cy.get('input[name="password2"]').type('senha_valida123');
        cy.get('button[type="submit"]').click();
  
        // Login com o novo usuário
        cy.visit(`${baseUrl}/login`);
        cy.get('input[name="email"]').type('usuario_valido@example.com');
        cy.get('input[name="password"]').type('senha_valida123');
        cy.get('button[type="submit"]').click();
  
        // Verifica se o novo usuário consegue acessar a página "Consórcio de Culturas"
        cy.visit(`${baseUrl}/rotacao/`); // Atualize o URL conforme necessário
        cy.contains('Consórcio de Culturas').should('be.visible'); // Verifica se a página carregou corretamente
    });
});
