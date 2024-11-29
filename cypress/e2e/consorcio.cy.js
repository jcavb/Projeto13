const adminData = {
    username: "admin",
    email: "admin@example.com",
    password: "1234",
    isAdmin: true,
};

beforeEach(() => {
    // Limpa o banco de dados e executa as migrações
    cy.exec('rm -f db.sqlite3'); // No Windows, usa 'del /f' para deletar
    cy.exec('python manage.py migrate');
    
    // Verifique se o servidor está funcionando antes de rodar os testes
    cy.request('http://127.0.0.1:8000') // Verifica se o servidor responde
      .its('status')
      .should('eq', 200);
});

describe('Testes de Condições da Cidade', () => {
    it('Admin: Deve acessar a página Consórcio de Culturas após login', () => {
        cy.visit('http://127.0.0.1:8000/login');
        
        // Login como Admin
        cy.get('input[name="email"]').type(adminData.email);
        cy.get('input[name="password"]').type(adminData.password);
        cy.get('button[type="submit"]').click();
  
        // Verifica se o admin consegue acessar a página "Consórcio de Culturas"
        cy.visit('http://127.0.0.1:8000/rotacao/'); // Atualize o URL conforme necessário
        cy.contains('Consórcio de Culturas').should('be.visible'); // Verifica se a página carregou corretamente
    });

    it('Novo Usuário: Deve acessar a página Consórcio de Culturas após login', () => {
        // Registro de novo usuário
        cy.visit('http://127.0.0.1:8000/signup');
        cy.get('input[name="username"]').type('usuario_valido');
        cy.get('input[name="email"]').type('usuario_valido@example.com');
        cy.get('input[name="password1"]').type('senha_valida123');
        cy.get('input[name="password2"]').type('senha_valida123');
        cy.get('button[type="submit"]').click();
  
        // Login com o novo usuário
        cy.visit('http://127.0.0.1:8000/login');
        cy.get('input[name="email"]').type('usuario_valido@example.com');
        cy.get('input[name="password"]').type('senha_valida123');
        cy.get('button[type="submit"]').click();
  
        // Verifica se o novo usuário consegue acessar a página "Consórcio de Culturas"
        cy.visit('http://127.0.0.1:8000/rotacao/'); // Atualize o URL conforme necessário
        cy.contains('Consórcio de Culturas').should('be.visible'); // Verifica se a página carregou corretamente
    });
});
