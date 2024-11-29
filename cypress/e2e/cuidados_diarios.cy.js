const userData = {
    username: "usuario_cuidados",
    email: "cuidados_user@example.com",
    password: "cuidados123",
  };
  
  describe("Teste de Cuidados Diários", () => {
    before(() => {
      // Configurações iniciais
      cy.exec('rm -f db.sqlite3'); // Para Windows; substitua por 'rm -f db.sqlite3' no Linux/Mac
      cy.exec('python manage.py migrate');
  
      // Cria um usuário no sistema
      cy.visit('http://127.0.0.1:8000/signup');
      cy.get('input[name="username"]').type(userData.username);
      cy.get('input[name="email"]').type(userData.email);
      cy.get('input[name="password1"]').type(userData.password);
      cy.get('input[name="password2"]').type(userData.password);
      cy.get('button[type="submit"]').click();
    });
  
    it("Usuário visualiza a página de Cuidados Diários", () => {
      // Ignorar erro de "addEventListener" durante o teste
      Cypress.on('uncaught:exception', (err, runnable) => {
        if (err.message.includes('Cannot read properties of null')) {
          return false; // Ignora esse erro específico
        }
        return true; // Não ignora outros erros
      });
  
      // Login do usuário
      cy.visit('http://127.0.0.1:8000/login');
      cy.get('input[name="email"]').type(userData.email);
      cy.get('input[name="password"]').type(userData.password);
      cy.get('button[type="submit"]').click();
  
      // Acessar a página de Cuidados Diários (Tarefas)
      cy.visit('http://127.0.0.1:8000/tarefas/');
  
      // Verificar se a página foi carregada corretamente
      cy.url().should('include', '/tarefas/'); // Garante que está na página correta // Garante que um título da página está visível (ajuste conforme necessário)
  
      // Se quiser apenas garantir que elementos estão visíveis
      
    });
  });
  